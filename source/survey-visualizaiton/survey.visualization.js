const H = require('../../utils/general.helper')
const CP = require('child_process')

/**
 * Replicate certain tool of a `structure size` decreased with `step`
 * @param {String} toolPath 
 * @param {Number} structSize 
 * @param {Number} step 
 * @returns {CP.ChildProcess|undefined}
 */
const createGeneration =
  (toolPath, structSize, step) =>
    CP
      .execFile('node', H.trace([toolPath, structSize]))
      .on(
        'exit',
        (code, signal) => code === 0 && structSize > 0
          ? createGeneration(toolPath, structSize - step)
          : H.trace('Generation is finished')
      )

/**
 * Run `visualizator`
 * @param {String} specificity 
 */
const visualizeExperiment =
  (specificity) =>
    CP.execFile(
      'python',
      ['benchmark-visualizer/benchmark_visualizer.py', specificity]
    )

module.exports = {
  visualizeExperiment,
  createGeneration
}