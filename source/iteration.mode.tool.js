require('module-alias/register')

const H = require('@general-helper')
const I = require('immutable')
const MI = require('mori')
const CLI_COLOR = require('cli-color')
const S_BENCHMARK = require('./benchmark-master/benchmark.master')
const STRUCTURE_SIZE = Number(require('dotenv').config().parsed.STRUCTURE_SIZE)

console.time(`${CLI_COLOR.bgWhiteBright('MORI.JS')}               STRUCTURE GENERATION`)
const MORI_LIST = MI.take(STRUCTURE_SIZE, MI.range())
console.timeEnd(`${CLI_COLOR.bgWhiteBright('MORI.JS')}               STRUCTURE GENERATION`)

console.time(`${CLI_COLOR.bgBlueBright('IMMUTABLE.JS')}          STRUCTURE GENERATION`)
const IMMUTABLE_LIST = I.Range().take(STRUCTURE_SIZE)
console.timeEnd(`${CLI_COLOR.bgBlueBright('IMMUTABLE.JS')}          STRUCTURE GENERATION`)

console.time(`${CLI_COLOR.bgGreenBright('NATIVE')}                STRUCTURE GENERATION`)
const NATIVE_LIST = Array(STRUCTURE_SIZE).fill(0).map((x, i) => i)
console.timeEnd(`${CLI_COLOR.bgGreenBright('NATIVE')}                STRUCTURE GENERATION`)

H.trace(
  S_BENCHMARK.getMeanBenchmark(
    8,
    () => MI.map(MI.identity, MORI_LIST)
  ),
  `- ${CLI_COLOR.bgWhiteBright('MORI.JS')} EXECUTION MEAN VALUE, milliseconds`
)

H.trace(
  S_BENCHMARK.getMeanBenchmark(
    8,
    () => IMMUTABLE_LIST.map(x => x)
  ),
  `- ${CLI_COLOR.bgBlueBright('IMMUTABLE.JS')} EXECUTION MEAN VALUE, milliseconds`
)

H.trace(
  S_BENCHMARK.getMeanBenchmark(
    8,
    () => NATIVE_LIST.map(x => x)
  ),
  `- ${CLI_COLOR.bgGreenBright('NATIVE')} EXECUTION MEAN VALUE, milliseconds`
)
