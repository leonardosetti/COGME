// COGME — JavaScript consolidado (substitui scripts inline)
// Cada bloco só roda quando o elemento correspondente existe no DOM.

(function () {
  // ---------- Auth: login / register ----------
  var form = document.getElementById('form');
  if (!form) return;

  var btn = document.getElementById('btn');
  var btnText = btn && btn.querySelector('.btn-text');
  var btnSpinner = btn && btn.querySelector('.spinner');
  var globalError = document.getElementById('global-error');

  function showFieldError(fieldName, message) {
    var input = form.querySelector('[name="' + fieldName + '"]');
    var errorEl = document.getElementById(fieldName + '-error');
    if (input) input.classList.add('invalid');
    if (errorEl) {
      errorEl.textContent = message;
      errorEl.classList.add('visible');
    }
  }

  function clearFieldErrors() {
    if (!form) return;
    form.querySelectorAll('.invalid').forEach(function (el) { el.classList.remove('invalid'); });
    form.querySelectorAll('.field-error.visible').forEach(function (el) { el.classList.remove('visible'); el.textContent = ''; });
  }

  function showGlobalError(message) {
    globalError.textContent = message;
    globalError.classList.remove('hidden');
  }

  function hideGlobalError() {
    globalError.classList.add('hidden');
    globalError.textContent = '';
  }

  form.addEventListener('submit', async function (e) {
    e.preventDefault();
    clearFieldErrors();
    hideGlobalError();

    btn.disabled = true;
    if (btnText) btnText.textContent = btnText.textContent === 'Entrar' ? 'Entrando…' : 'Criando…';
    if (btnSpinner) btnSpinner.classList.remove('hidden');

    var payload = {};
    if (form['identifier']) payload.identifier = form['identifier'].value;
    if (form['password']) payload.password = form['password'].value;
    if (form['name']) payload.name = form['name'].value;

    var url = form.action || (payload.password && form['identifier'] ? '/v1/auth/login' : '/v1/auth/register');
    try {
      var res = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify(payload),
      });

      if (!res.ok) {
        var data = await res.json();
        var details = (data && data.error && data.error.details) || [];
        if (details.length) {
          details.forEach(function (d) { showFieldError(d.field, d.message); });
        } else {
          showGlobalError((data && data.error && data.error.message) || 'Não foi possível completar a operação.');
        }
        return;
      }

      window.location.href = '/';
    } catch (err) {
      showGlobalError('Não foi possível conectar à API.');
    } finally {
      btn.disabled = false;
      if (btnText) btnText.textContent = btn.dataset.original || (btnText.textContent === 'Entrando…' ? 'Entrar' : 'Criar conta');
      if (btnSpinner) btnSpinner.classList.add('hidden');
    }
  });

  form.querySelectorAll('.input').forEach(function (el) {
    el.addEventListener('input', function () {
      if (el.classList.contains('invalid')) {
        el.classList.remove('invalid');
        var errorEl = document.getElementById(el.name + '-error');
        if (errorEl) { errorEl.classList.remove('visible'); errorEl.textContent = ''; }
      }
    });
  });
})();

// ---------- Auth: reset ----------
(function () {
  var form = document.querySelector('form');
  if (!form) return;
  var password = document.getElementById('new_password');
  var confirm = document.getElementById('confirm_password');
  if (!password || !confirm) return;

  form.addEventListener('submit', function (e) {
    if (password.value !== confirm.value) {
      e.preventDefault();
      alert('As senhas não coincidem.');
      confirm.focus();
    }
  });
})();

// ---------- Frontend: invoice form ----------
(function () {
  var form = document.getElementById('form');
  if (!form) return;

  var btn = document.getElementById('btn');
  var btnText = btn && btn.querySelector('.btn-text');
  var btnSpinner = btn && btn.querySelector('.spinner');
  var result = document.getElementById('result');
  var qtyWrap = document.getElementById('qty-wrap');
  var stale = document.getElementById('stale');
  var notice = document.getElementById('notice');
  var errorSummary = document.getElementById('error-summary');
  var errorSummaryList = document.getElementById('error-summary-list');
  var globalError = document.getElementById('global-error');

  var issueDate = document.getElementById('issue_date');
  if (issueDate && !issueDate.value) {
    var today = new Date().toISOString().split('T')[0];
    issueDate.value = today;
  }

  function toggleQty() {
    if (!form || !form['sim-regime']) return;
    var fixed = form['sim-regime'].value === 'fixed';
    var qtyInput = form['sim-quantity'];
    if (fixed) {
      qtyWrap.classList.add('hidden');
      if (qtyInput) qtyInput.required = false;
    } else {
      qtyWrap.classList.remove('hidden');
      if (qtyInput) qtyInput.required = true;
    }
  }
  if (form && form['sim-regime']) {
    form['sim-regime'].addEventListener('change', toggleQty);
    toggleQty();
  }

  function money(v) { return v ? Number(v).toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) : v; }

  function showFieldError(fieldName, message) {
    var input = form.querySelector('[name="' + fieldName + '"]');
    var errorEl = document.getElementById(fieldName + '-error');
    if (input) input.classList.add('invalid');
    if (errorEl) {
      errorEl.textContent = message;
      errorEl.classList.add('visible');
    }
  }

  function clearFieldErrors() {
    if (!form) return;
    form.querySelectorAll('.invalid').forEach(function (el) { el.classList.remove('invalid'); });
    form.querySelectorAll('.field-error.visible').forEach(function (el) { el.classList.remove('visible'); el.textContent = ''; });
  }

  function showGlobalError(message, showRetry) {
    globalError.textContent = message;
    globalError.classList.remove('hidden');
    var existingRetry = globalError.querySelector('.retry');
    if (existingRetry) existingRetry.remove();
    if (showRetry) {
      var retry = document.createElement('button');
      retry.type = 'button';
      retry.textContent = 'Tentar novamente';
      retry.className = 'retry btn btn-secondary';
      retry.style.marginTop = 'var(--space-3)';
      retry.onclick = function () {
        retry.remove();
        globalError.classList.add('hidden');
        if (btn) { btn.disabled = false; btnText.textContent = 'Gerar invoice em PDF'; btnSpinner.classList.add('hidden'); }
      };
      globalError.appendChild(retry);
    }
  }

  function hideGlobalError() {
    globalError.classList.add('hidden');
    globalError.textContent = '';
  }
})();
