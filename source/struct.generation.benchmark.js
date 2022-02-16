require('child_process').execFileSync('node', ['utils/general-cleaner/general.cleaner.tool.js'])

const H = require('../utils/general.helper')
const ENV = H.eitherObjValuesToNumber(require('dotenv').config().parsed)
const MORI = require('mori')
const DS_GEN = require('./struct-master/data-struct/data.struct.generator')
const Benchmark = require('benchmark')
const BS_GEN_HANDLER = require('./struct-master/bench-suite/bench.suite.generator.handler')

new Benchmark
  .Suite(`${ENV.DELIMITER} Sturcture Generation. Structure size: ${H.prettyInt(ENV.STRUCT_SIZE)}`)
  .add('Mori       ', () => MORI.intoArray(DS_GEN.constructMoriList(ENV.STRUCT_SIZE)))
  .add('Lazy       ', () => DS_GEN.constructLazyList(ENV.STRUCT_SIZE).toArray())
  .add('Native     ', () => DS_GEN.constructNativeList(ENV.STRUCT_SIZE))
  .add('Immutable  ', () => DS_GEN.constructImmutableList(ENV.STRUCT_SIZE).toArray())
  .on('start', (event) => BS_GEN_HANDLER.whenFlagWriteFile(true, event.currentTarget.name, `Struct.Size.${ENV.STRUCT_SIZE}`, 'generation'))
  .on('cycle', (event) => BS_GEN_HANDLER.whenFlagWriteFile(true, `${ENV.DELIMITER}    ${String(event.target)}`, `Struct.Size.${ENV.STRUCT_SIZE}`, 'generation'))
  .on('complete', (event) => BS_GEN_HANDLER.whenFlagWriteFile(true, `${ENV.DELIMITER}  Fastest is ${event.currentTarget.filter("fastest").map("name")}`, `Struct.Size.${ENV.STRUCT_SIZE}`, 'generation'))
  .run()
