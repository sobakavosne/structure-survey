const H = require('../utils/general.helper')
const R = require('ramda')
const ENV = H.eitherObjValuesToNumber(require('dotenv').config().parsed)
const MORI = require('mori')
const CLI_COLOR = require('cli-color')
const BENCH_MASTER = require('./bench-master/bench.master')
const BENCH_MASTER_STRUCT = require('./bench-master/bench.master.struct')
const BENCH_MASTER_HELPER = require('./bench-master/bench.master.helper')

const I_LIST = BENCH_MASTER.baseTimedFncIO(
  CLI_COLOR.bgBlueBright('IMMUTABLE.JS'),
  ': STRUCTURE GENERATION\t',
  BENCH_MASTER_STRUCT.constructImmutableList,
  ENV.STRUCTURE_SIZE
)

const MORI_LIST = BENCH_MASTER.baseTimedFncIO(
  CLI_COLOR.bgWhiteBright('MORI.JS'),
  ': STRUCTURE GENERATION\t',
  BENCH_MASTER_STRUCT.constructMoriList,
  ENV.STRUCTURE_SIZE
)

const NATIVE_LIST = BENCH_MASTER.baseTimedFncIO(
  CLI_COLOR.bgGreenBright('NATIVE'),
  ': STRUCTURE GENERATION\t',
  BENCH_MASTER_STRUCT.constructNativeList,
  ENV.STRUCTURE_SIZE
)

const I_ARRAY = BENCH_MASTER.baseTimedFncIO(
  CLI_COLOR.bgBlueBright('IMMUTABLE.JS'),
  ': CONVERT INTO JS ARRAY\t',
  () => I_LIST.toArray()
)

const MORI_ARRAY = BENCH_MASTER.baseTimedFncIO(
  CLI_COLOR.bgWhiteBright('MORI.JS'),
  ': CONVERT INTO JS ARRAY\t',
  MORI.intoArray,
  MORI_LIST
)

const identity = (element) => element

const I_LIST_PROCESSED = H.trace(
  BENCH_MASTER.processStruct(
    ENV.ITERATIONS,
    () => I_LIST.map(identity)
  ),
  BENCH_MASTER_HELPER.constructMeanBenchmarkDescription('IMMUTABLE.JS')
)

const MORI_LIST_PROCESSED = H.trace(
  BENCH_MASTER.processStruct(
    ENV.ITERATIONS,
    () => MORI.map(identity, MORI_LIST)
  ),
  BENCH_MASTER_HELPER.constructMeanBenchmarkDescription('MORI.JS')
)

const NATIVE_LIST_PROCESSED = H.trace(
  BENCH_MASTER.processStruct(
    ENV.ITERATIONS,
    () => NATIVE_LIST.map(identity)
  ),
  BENCH_MASTER_HELPER.constructMeanBenchmarkDescription('NATIVE')
)

const CONVERTED_IMMUTABLE_LIST = BENCH_MASTER.baseTimedFncIO(
  CLI_COLOR.bgBlueBright('IMMUTABLE.JS'),
  ': CONVERT PROCESSED STRUCTURE INTO JS ARRAY',
  () => R.last(I_LIST_PROCESSED)
)

const CONVERTED_MORI_LIST = BENCH_MASTER.baseTimedFncIO(
  CLI_COLOR.bgWhiteBright('MORI.JS'),
  ': CONVERT PROCESSED STRUCTURE INTO JS ARRAY',
  MORI.intoArray,
  H.trace(R.head(MORI_LIST_PROCESSED)[1], 'MORILIST')[1]
)

H.trace(
  CONVERTED_MORI_LIST,
  'CONVERTED MORI LIST',
  CONVERTED_IMMUTABLE_LIST,
  'CONVERTED IMMUTABLE LIST'
)
