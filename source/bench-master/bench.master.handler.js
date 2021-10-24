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
      ([start, _]) => M.IO(() => performance.now() - start)
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

module.exports = {
  replicateExecution: R.curry(replicateExecution),
  timedFnc: R.curry(timedFnc)
}
