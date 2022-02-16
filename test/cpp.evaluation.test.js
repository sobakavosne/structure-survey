/**
 * Clear previous initialization (remove log/, build/)
 */
require('child_process').execFileSync('node', ['utils/general-cleaner/general.cleaner.tool.js'])
/**
 * Rebuild C++ addon
 */
require('child_process').execSync('node-gyp configure rebuild', { stdio: 'ignore' })

const CPP_A = require('../build/Release/init')

test(`C++ 'Identity' function is equal to JS 'identity'`, () => expect(CPP_A.identity(10)).toEqual(10))

test(`C++ 'Add'      function is equal to JS 'add'     `, () => expect(CPP_A.add(10, 10)).toEqual(10 + 10))
