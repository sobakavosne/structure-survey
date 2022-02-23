const R = require('ramda')
const H = require('../../../utils/general.helper')
const ENV = H.eitherObjValuesToNumber(require('dotenv').config().parsed)
const SG_HANDLER = require('./suite.generator.handler')

/**
 * Construct **`Benchmark Suite`**'s with mapping over structures of different `k` sizes `n` times
 * @example Matrix with pseudocode that is generated:
 * - [
 * -    [Suite(ITER-0*STEP, STRUCT-0*STEP), ..., Suite(ITER-0*STEP, STRUCT-k*STEP)],
 * -    ...,
 * -    [Suite(ITER-n*STEP, STRUCT-0*STEP), ..., Suite(ITER-n*STEP, STRUCT-k*STEP)]
 * - ]
 * @param {Function} fnc Mapping `function`
 * @param {String} fncName Function name
 * @param {String} lib Library name
 * @param {Boolean} isFile Flag to choose log branch: write to console <-> write to file
 * @returns {Array<Array<Benchmark.Suite>>}
 */
const numListSuiteIO =
  (fnc, fncName, lib, isFile) =>
    R.pipe(
      SG_HANDLER.makeMatrixList,
      SG_HANDLER.makeNumListSuiteMatrixList(fnc, fncName, lib, isFile, ENV.DELIMITER),
      SG_HANDLER.runSuiteMatrixList
    )(ENV.ITER_MAX, ENV.ITER_STEP, ENV.STRUCT_MAX, ENV.STRUCT_STEP)

module.exports = {
  numListSuiteIO
}