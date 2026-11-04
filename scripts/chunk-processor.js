const fs = require('fs');
const path = require('path');

const inputFile = path.join(__dirname, '../docs/decisoes/ADR-006-inteligencia-sdd.md');
const outputFilePrefix = path.join(__dirname, '../docs/decisoes/ADR-006-chunk-');

const chunkSize = 1000;
let content = fs.readFileSync(inputFile, 'utf-8');
let lines = content.split('\n');

for (let i = 0; i < lines.length; i += chunkSize) {
  let chunk = lines.slice(i, i + chunkSize).join('\n');
  fs.writeFileSync(outputFilePrefix + (Math.floor(i/1000) + 1) + '.md', chunk);
}

console.log('Split complete');