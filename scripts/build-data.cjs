const fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'..');const data=JSON.parse(fs.readFileSync(path.join(root,'content.json'),'utf8'));
fs.writeFileSync(path.join(root,'data.js'),'window.NAHW = '+JSON.stringify(data,null,2)+';\n');
console.log('Updated data.js from content.json; vocabulary.js and terms.js are separate resources.');
