const H = require('../../utils/general.helper')
const ENV = H.eitherObjValuesToNumber(require('dotenv').config().parsed)

const CP = require('child_process')

/**
 * Benchmark grid 
 * @param {String} toolPath 
 */
const createBenchGridIO =
  (toolPath) =>
    CP.execFile('node', [toolPath, ENV.STRUCT_MAX, ENV.STRUCT_STEP])
      // .on('exit', (code, signal) => CP.execFile('node', [toolPath, ENV.STRUCT_MAX_2, ENV.STRUCT_STEP_2]))
      // .on('exit', (code, signal) => CP.execFile('node', [toolPath, ENV.STRUCT_MAX_3, ENV.STRUCT_STEP_3]))

/**
 * Run `visualizator`
 * @param {String} toolPath 
 */
const visualizeExperimentIO =
  (toolPath) =>
    CP.execFile('python', [toolPath])

module.exports = {
  visualizeExperimentIO,
  createBenchGridIO
}