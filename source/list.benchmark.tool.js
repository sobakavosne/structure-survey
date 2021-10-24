const H = require('../utils/general.helper')
const R = require('ramda')
const ENV = H.eitherObjValuesToNumber(require('dotenv').config().parsed)
const MORI = require('mori')
const CLI_COLOR = require('cli-color')
const BENCH_MASTER = require('./bench-master/bench.master')
const BENCH_MASTER_STRUCT = require('./bench-master/bench.master.struct')
const BENCH_MASTER_HELPER = require('./bench-master/bench.master.helper')

const I_LIST = BENCH_MASTER.baseTimedFnc(
  CLI_COLOR.bgBlueBright('IMMUTABLE.JS'),
  ': STRUCTURE GENERATION\t',
  BENCH_MASTER_STRUCT.constructImmutableList,
  ENV.STRUCTURE_SIZE
)

const MORI_LIST = BENCH_MASTER.baseTimedFnc(
  CLI_COLOR.bgWhiteBright('MORI.JS'),
  ': STRUCTURE GENERATION\t',
  BENCH_MASTER_STRUCT.constructMoriList,
  ENV.STRUCTURE_SIZE
)

const NATIVE_LIST = BENCH_MASTER.baseTimedFnc(
  CLI_COLOR.bgGreenBright('NATIVE'),
  ': STRUCTURE GENERATION\t',
  BENCH_MASTER_STRUCT.constructNativeList,
  ENV.STRUCTURE_SIZE
)

const I_ARRAY = BENCH_MASTER.baseTimedFnc(
  CLI_COLOR.bgBlueBright('IMMUTABLE.JS'),
  ': CONVERT INTO JS ARRAY\t',
  () => I_LIST.toArray()
)

const MORI_ARRAY = BENCH_MASTER.baseTimedFnc(
  CLI_COLOR.bgWhiteBright('MORI.JS'),
  ': CONVERT INTO JS ARRAY\t',
  MORI.intoArray,
  MORI_LIST
)

H.trace(
  BENCH_MASTER.getMeanBenchmark(
    ENV.ITERATIONS,
    () => I_LIST.map(R.identity)
  ),
  BENCH_MASTER_HELPER.constructMeanBenchmarkDescription('IMMUTABLE.JS')
)

H.trace(
  BENCH_MASTER.getMeanBenchmark(
    ENV.ITERATIONS,
    () => MORI.map(R.identity, MORI_LIST)
  ),
  BENCH_MASTER_HELPER.constructMeanBenchmarkDescription('MORI.JS')
)

H.trace(
  BENCH_MASTER.getMeanBenchmark(
    ENV.ITERATIONS,
    () => NATIVE_LIST.map(R.identity)
  ),
  BENCH_MASTER_HELPER.constructMeanBenchmarkDescription('NATIVE')
)
