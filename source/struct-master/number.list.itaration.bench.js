/**
 * ITER_MAX, ITER_STEP, STRUCT_MAX, STRUCT_STEP - command line options required
 * A - C++ Addon abbreviation
 */

/**
 * Clear previous initialization (remove log/, build/)
 */
require('child_process').execFileSync('node', ['utils/general-cleaner/general.cleaner.tool.js'])
/**
 * Build C++ addon
 */
require('child_process').execSync('node-gyp configure rebuild', { stdio: 'ignore' })

const R = require('ramda')
const D = require('lodash')
const U = require('underscore')
const N = require('../native/native.functions')
const A = require('../../build/Release/init')
const SUITE_GENERATOR = require('./bench-suite/suite.generator')

SUITE_GENERATOR
  .numListSuiteIO(A.identity, 'Identity', `C++`, true)

SUITE_GENERATOR
  .numListSuiteIO(R.identity, 'Identity', 'Ramda', true)

SUITE_GENERATOR
  .numListSuiteIO(N.identity, 'Identity', `Native`, true)

SUITE_GENERATOR
  .numListSuiteIO(D.identity, 'Identity', 'Lodash', true)

SUITE_GENERATOR
  .numListSuiteIO(U.identity, 'Identity', 'Underscore', true)
