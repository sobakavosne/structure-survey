require('module-alias/register')

const H = require('@general.helper')
const DS = require('../data-struct/data.struct')
const ENV = H.eitherObjValuesToNumber(require('dotenv').config().parsed)
const MORI = require('mori')
const Benchmark = require('benchmark')
const BS_GEN_HANDLER = require('./bench.suite.generator.handler')

/**
 * Construct **`Benchmark Suite`** with mapping over structures `n` times
 * @param {Function} fnc Mapping `function`
 * @param {Number} iterations Number of iterations over a `struct` via function 
 * @param {String} suite `Suit` description
 * @param {Number} structSize 
 * @param {Boolean} isFile 
 */
const iterSuiteConstructor =
  (fnc, iterations, suite, structSize, isFile) =>
    new Benchmark
      .Suite(`${ENV.DELIMITER} ${iterations} iterations via  ${suite}. Structure size: ${H.prettyInt(structSize)}`)
      .add('Mori       ', () => MORI.intoArray(BS_GEN_HANDLER.repeatMoriMap(iterations, DS.M_LIST, fnc)))
      .add('Lazy       ', () => BS_GEN_HANDLER.repeatMap(iterations, DS.L_LIST, fnc).toArray())
      .add('Native     ', () => BS_GEN_HANDLER.repeatMap(iterations, DS.N_LIST, fnc))
      .add('Immutable  ', () => BS_GEN_HANDLER.repeatMap(iterations, DS.I_LIST, fnc).toArray())
      .on('start', (event) => BS_GEN_HANDLER.whenFlagWriteFile(isFile, event.currentTarget.name, `${suite}.iter.${iterations}`, 'iteration'))
      .on('cycle', (event) => BS_GEN_HANDLER.whenFlagWriteFile(isFile, `${ENV.DELIMITER}    ${String(event.target)}`, `${suite}.iter.${iterations}`, 'iteration'))
      .on('complete', (event) => BS_GEN_HANDLER.whenFlagWriteFile(isFile, `${ENV.DELIMITER}  Fastest is ${event.currentTarget.filter("fastest").map("name")}`, `${suite}.iter.${iterations}`, 'iteration'))

module.exports = {
  iterSuiteConstructor
}
