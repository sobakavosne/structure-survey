require('module-alias/register')

const H = require('@general-helper')
const DS = require('../data-struct/data.struct')
const MORI = require('mori')
const Benchmark = require('benchmark')
const BS_GEN_HANDLER = require('./bench.suite.generator.handler')

/**
 * Construct **`Benchmark Suite`** with mapping over structures `n` times
 * @param {Function} fnc Mapping `function`
 * @param {Number} iterations Number of iterations over a `struct` via function 
 * @param {String} description `Suit` description
 * @param {Number} structSize 
 */
const suiteConstructor =
  (fnc, iterations, description, structSize) =>
    new Benchmark
      .Suite(`\n${iterations} iterations via  ${description}. Structure size: ${H.prettyInt(structSize)}`)
      .add('Native     ', () => BS_GEN_HANDLER.repeatMap(iterations, DS.N_LIST, fnc))
      .add('Mori       ', () => MORI.intoArray(BS_GEN_HANDLER.repeatMoriMap(iterations, DS.M_LIST, fnc)))
      .add('Immutable  ', () => BS_GEN_HANDLER.repeatMap(iterations, DS.I_LIST, fnc).toArray())
      .add('Lazy       ', () => BS_GEN_HANDLER.repeatMap(iterations, DS.L_LIST, fnc).toArray())
      .on('start', (event) => H.trace(event.currentTarget.name))
      .on('cycle', (event) => H.trace(`   ${String(event.target)}`))
      .on('complete', (event) => H.trace(` Fastest is ${event.currentTarget.filter("fastest").map("name")}`))

module.exports = {
  suiteConstructor
}
