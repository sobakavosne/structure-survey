const H = require('../../../utils/general.helper')
const MORI = require('mori')
const DS_GEN = require('../data-struct/data.struct.generator')
const SG_HELPER = require('./suite.generator.helper')
const Benchmark = require('benchmark')

/**
 * Construct `Stuite` matrix
 * @param {Number} iterMax Maximum number of iterations over a `struct` via function 
 * @param {Number} iterStep Iteration step decrement
 * @param {Number} structSize Maximum structure size
 * @param {Number} structStep Structure step decrement
 */
const makeMatrixList =
  (iterMax, iterStep, structSize, structStep) =>
    new Array(Math.round(1 + iterMax / iterStep))
      .fill(0)
      .map((x, i) => i * iterStep)
      .map(
        iterations =>
          new Array(Math.round(1 + structSize / structStep))
            .fill(0)
            .map((x, i) => [iterations, i * structStep])
      )

/**
 * @param {Function} fnc 
 * @param {String} fncName 
 * @param {String} lib  
 * @param {Boolean} isFile 
 * @param {String} delimiter
 * @param {Array<Array<Array<Number>>>} matrixList
 * @returns {Array<Array<Benchmark.Suite>>}
 */
const makeNumListSuiteMatrixList =
  (fnc, fncName, lib, isFile, delimiter) => (matrixList) =>
    matrixList.map(
      x => x.map(
        ([iterations, structSize]) =>
          new Benchmark
            .Suite(`${delimiter} ${iterations} iterations via  ${fncName}. Structure size: ${H.prettyInt(structSize)}`)
            .add('Mori       ', () => MORI.intoArray(SG_HELPER.repeatMoriMap(iterations, DS_GEN.constructNumMList(structSize), fnc)))
            .add('Lazy       ', () => SG_HELPER.repeatMap(iterations, DS_GEN.constructNumLList(structSize), fnc).toArray())
            .add('Native     ', () => SG_HELPER.repeatMap(iterations, DS_GEN.constructNumNList(structSize), fnc))
            .add('Immutable  ', () => SG_HELPER.repeatMap(iterations, DS_GEN.constructNumIList(structSize), fnc).toArray())
            .on('start', (event) => SG_HELPER.whenFlagWriteFile(
              isFile,
              event.currentTarget.name,
              fncName,
              lib,
              iterations,
              structSize,
              'number-list'))
            .on('cycle', (event) => SG_HELPER.whenFlagWriteFile(
              isFile,
              `${delimiter}    ${String(event.target)}`,
              fncName,
              lib,
              iterations,
              structSize,
              'number-list'))
            .on('complete', (event) => SG_HELPER.whenFlagWriteFile(
              isFile,
              `${delimiter}  Fastest is ${event.currentTarget.filter("fastest").map("name")}`,
              fncName,
              lib,
              iterations,
              structSize,
              'number-list')
            )
      )
    )

/**
 * @param {Array<Array<Benchmark.Suite>>} suiteMatrix 
 */
const runSuiteMatrixList =
  (suiteMatrix) =>
    suiteMatrix.map(
      suiteList => suiteList.map(
        suite => suite.run()
      )
    )

module.exports = {
  makeNumListSuiteMatrixList,
  runSuiteMatrixList,
  makeMatrixList
}