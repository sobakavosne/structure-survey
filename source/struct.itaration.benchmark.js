const H = require('../utils/general.helper')
const R = require('ramda')
const BS = require('./struct-master/bench-suite/bench.suite')
const ENV = H.eitherObjValuesToNumber(require('dotenv').config().parsed)
const CPP_A = require('../build/Release/init')

BS
  .suiteConstructor(x => x + 1, 1, `Native 'Add'`, ENV.STRUCT_SIZE)
  .run()

BS
  .suiteConstructor(R.add(1), 1, `Ramda 'Add'`, ENV.STRUCT_SIZE)
  .run()

BS
  .suiteConstructor(x => CPP_A.add(1, x), 1, `C++ 'Add'`, ENV.STRUCT_SIZE)
  .run()

BS
  .suiteConstructor(x => x, 5, `Native 'Identity'`, ENV.STRUCT_SIZE)
  .run()

BS
  .suiteConstructor(R.identity, 5, `Ramda 'Identity'`, ENV.STRUCT_SIZE)
  .run()

BS
  .suiteConstructor(CPP_A.identity, 5, `C++ 'Identity'`, ENV.STRUCT_SIZE)
  .run()

BS
  .suiteConstructor(x => x, 10, `Native 'Identity'`, ENV.STRUCT_SIZE)
  .run()

BS
  .suiteConstructor(R.identity, 10, `Ramda 'Identity'`, ENV.STRUCT_SIZE)
  .run()

BS
  .suiteConstructor(CPP_A.identity, 10, `C++ 'Identity'`, ENV.STRUCT_SIZE)
  .run()
