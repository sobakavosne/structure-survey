require('module-alias')

const H = require('@general-helper')
const M = require('monet')
const R = require('ramda')

/**
 * `Function` returns execution time, `ms`
 * @param {Function} fnc 
 * @param  {...any} args 
 */
const timedFnc =
  (fnc, ...args) =>
    M.IO(
      () => performance.now()
    ).bind(
      (start) => M.IO(() => [start, fnc(...args)])
    ).bind(
      ([start, result]) => M.IO(() => [performance.now() - start, result])
    ).run()

/**
 * Repeat `n` times `fnc` execution
 * @param {Number} n times 
 * @param {Function} fnc function for repetition
 * @param  {...any} args `fnc` arguments 
 * @returns {Array} List of `fnc` results 
 */
const replicateExecution =
  (n, fnc, ...args) =>
    Array(n).fill(0).map(x => fnc(...args))

/**
 * @param {Array} timedResult 
 */
const processTimedResult =
  (timedResult) => [
    R.head(timedResult),
    R.compose(R.map(([time, struct]) => time), R.tail)(timedResult)
  ]

/**
 * @param {Array} processedResult 
 */
const calculateMeanBench =
  (processedResult) => [
    R.head(processedResult),
    R.compose(R.sum, R.tail)(processedResult)
  ]

module.exports = {
  replicateExecution: R.curry(replicateExecution),
  timedFnc: R.curry(timedFnc),
  processTimedResult,
  calculateMeanBench
}
