/**
 * Clear previous initialization (remove log/, build/)
 */
require('child_process').execFileSync('node', ['utils/general-cleaner/general.cleaner.tool.js'])
/**
 * Build C++ addon
 */
require('child_process').execSync('node-gyp configure rebuild', { stdio: 'ignore' })

const H = require('../utils/general.helper')
const R = require('ramda')
const BS = require('./struct-master/bench-suite/bench.suite')
const ENV = H.eitherObjValuesToNumber(require('dotenv').config().parsed)
const CPP_A = require('../build/Release/init')

BS
  .iterSuiteConstructor(x => x + 1, 1, `Native.'Add'`, ENV.STRUCT_SIZE, true)
  .run()

BS
  .iterSuiteConstructor(R.add(1), 1, `Ramda.'Add'`, ENV.STRUCT_SIZE, true)
  .run()

BS
  .iterSuiteConstructor(x => CPP_A.add(1, x), 1, `C++.'Add'`, ENV.STRUCT_SIZE, true)
  .run()

BS
  .iterSuiteConstructor(x => x, 5, `Native.'Identity'`, ENV.STRUCT_SIZE, true)
  .run()

BS
  .iterSuiteConstructor(R.identity, 5, `Ramda.'Identity'`, ENV.STRUCT_SIZE, true)
  .run()

BS
  .iterSuiteConstructor(CPP_A.identity, 5, `C++.'Identity'`, ENV.STRUCT_SIZE, true)
  .run()

BS
  .iterSuiteConstructor(x => x, 10, `Native.'Identity'`, ENV.STRUCT_SIZE, true)
  .run()

BS
  .iterSuiteConstructor(R.identity, 10, `Ramda.'Identity'`, ENV.STRUCT_SIZE, true)
  .run()

BS
  .iterSuiteConstructor(CPP_A.identity, 10, `C++.'Identity'`, ENV.STRUCT_SIZE, true)
  .run()
