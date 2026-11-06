(function () {
  var form = document.getElementById('form');
  var btn = document.getElementById('btn');
  var error = document.getElementById('error');
  var globalError = document.getElementById('global-error');
  var result = document.getElementById('result');
  var qtyWrap = document.getElementById('qty-wrap');
  var notice = document.getElementById('notice');
  var stale = document.getElementById('stale');

  if (document.getElementById('issue_date')) {
    document.getElementById('issue_date').valueAsDate = new Date();
  }

  function toggleQty() {
    if (!form || !form.sim_regime) return;
    var fixed = form.sim_regime.value === 'fixed';
    if (qtyWrap) qtyWrap.style.display = fixed ? 'none' : 'block';
    if (form.sim_quantity) form.sim_quantity.required = !fixed;
  }
  if (form && form.sim_regime) {
    form.sim_regime.addEventListener('change', toggleQty);
    toggleQty();
  }

  function showFieldError(id, message) {
    var el = document.getElementById(id);
    if (!el) return;
    var existing = document.getElementById(id + '-err');
    el.classList.add('invalid');
    if (!existing && message) {
      var div = document.createElement('div');
      div.id = id + '-err';
      div.className = 'field-error';
      div.textContent = message;
      el.parentNode.insertBefore(div, el.nextSibling);
    } else if (existing) {
      existing.textContent = message || '';
      existing.style.display = message ? '' : 'none';
    }
  }

  function clearFieldErrors() {
    if (!form) return;
    form.querySelectorAll('.invalid').forEach(function (el) { el.classList.remove('invalid'); });
    form.querySelectorAll('.field-error').forEach(function (el) { el.remove(); });
  }

  function money(v) {
    return v ? Number(v).toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) : v;
  }

  if (form) {
    form.addEventListener('submit', async function (e) {
      e.preventDefault();
      clearFieldErrors();
      if (error) { error.style.display = 'none'; }
      if (globalError) { globalError.style.display = 'none'; globalError.textContent = ''; }
      if (result) result.style.display = 'none';
      if (notice) notice.textContent = '';
      if (stale) { stale.style.display = 'none'; }
      if (btn) { btn.disabled = true; btn.textContent = 'Gerando…'; }

      var payload = {
        simulation: {
          currency: form['sim-currency'].value,
          regime: form['sim-regime'].value,
          amount: form['sim-amount'].value,
          quantity: form['sim-regime'].value === 'fixed' ? null : form['sim-quantity'].value,
          spread_pct: form['sim-spread_pct'].value,
          iof_pct: form['sim-iof_pct'].value,
        },
        issuer: {
          name: document.getElementById('issuer-name').value,
          tax_id: document.getElementById('issuer-tax_id').value || null,
          address: document.getElementById('issuer-address').value || null,
        },
        client: {
          name: document.getElementById('client-name').value,
          tax_id: document.getElementById('client-tax_id').value || null,
          address: document.getElementById('client-address').value || null,
        },
        invoice_number: document.getElementById('invoice_number').value,
        issue_date: document.getElementById('issue_date').value,
        description: document.getElementById('description').value,
      };

      try {
        var res = await fetch('/v1/invoice', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload),
        });
        if (res.status === 503) {
          var data = await res.json();
          if (globalError) {
            globalError.textContent = (data && data.error && data.error.message) || 'Serviço indisponível. Tente novamente.';
            globalError.style.display = 'block';
          }
          var retry = document.createElement('button');
          retry.type = 'button';
          retry.textContent = 'Tentar novamente';
          retry.className = 'retry';
          retry.onclick = function () {
            retry.remove();
            if (btn) { btn.disabled = false; btn.textContent = 'Gerar invoice em PDF'; };
          };
          if (globalError) globalError.appendChild(retry);
          return;
        }
        if (!res.ok) {
          var data = await res.json();
          var details = (data && data.error && data.error.details) || [];
          if (details.length) {
            details.forEach(function (d) { showFieldError(d.field, d.message); });
            if (error) { error.textContent = 'Corrija os campos destacados.'; error.style.display = 'block'; }
          } else {
            if (error) { error.textContent = (data && data.error && data.error.message) || 'Dados inválidos.'; error.style.display = 'block'; }
          }
          return;
        }
        var blob = await res.blob();
        var url = URL.createObjectURL(blob);
        var a = document.createElement('a');
        a.href = url;
        var disp = res.headers.get('content-disposition') || '';
        var m = disp.match(/filename="([^"]+)"/);
        a.download = m ? m[1] : 'invoice.pdf';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);

        if (document.getElementById('r-invoice_number')) document.getElementById('r-invoice_number').textContent = payload.invoice_number;
        if (document.getElementById('r-issue_date')) document.getElementById('r-issue_date').textContent = payload.issue_date;
        if (document.getElementById('r-issuer')) document.getElementById('r-issuer').textContent = payload.issuer.name;
        if (document.getElementById('r-client')) document.getElementById('r-client').textContent = payload.client.name;
        if (document.getElementById('r-net_brl')) document.getElementById('r-net_brl').textContent = 'R$ ' + money(payload.simulation.amount) + ' (recálculo no servidor)';
        if (notice) notice.textContent = 'Invoice gerada. Verifique o PDF baixado antes de usar.';
        if (result) result.style.display = 'block';
      } catch (err) {
        if (globalError) { globalError.textContent = 'Não foi possível conectar à API.'; globalError.style.display = 'block'; }
      } finally {
        if (btn) { btn.disabled = false; btn.textContent = 'Gerar invoice em PDF'; }
      }
    });
  }
})();
