const fs = require('fs');

const archivos = ['README.md', 'LICENSE', 'CONTRIBUTING.md'];
let faltan = 0;

for (const f of archivos) {
  if (fs.existsSync(f)) {
    console.log(`OK: ${f} existe`);
  } else {
    console.log(`FALTA: ${f}`);
    faltan++;
  }
}

if (faltan > 0) {
  console.log('::error::Falta documentación');
  process.exit(1);
}