/**
 * STRUCT_MAX, STRUCT_STEP - command line options required
 * A - C++ Addon abbreviation
 */

/**
 * Clear previous initialization (remove log/, build/)
 */
// require('child_process').execFileSync('node', ['utils/general-cleaner/general.cleaner.tool.js'])
/**
 * Build C++ addon
 */
// require('child_process').execSync('node-gyp configure rebuild', { stdio: 'ignore' })

const R = require('ramda')
const D = require('lodash')
const U = require('underscore')
const N = require('../native/native.functions')
const A = require('../../build/Release/init')
const SUITE_GENERATOR = require('./bench-suite/suite.generator')

const IDENTITY_LIB_FNCS = [
  { fnc: A.add, name: 'C++' },
  { fnc: R.add, name: 'Ramda' },
  { fnc: N.add, name: 'Native' },
  { fnc: D.add, name: 'Lodash' },
  { fnc: U.add, name: 'Underscore' }
]

R.map(
  (libFnc) => SUITE_GENERATOR.numListSuiteIO(libFnc.fnc, 'Identity', libFnc.name),
  IDENTITY_LIB_FNCS
)
