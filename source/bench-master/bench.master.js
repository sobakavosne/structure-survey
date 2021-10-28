require('module-alias/register')

const H = require('@general-helper')
const R = require('ramda')
const M = require('monet')
const N_BENCHMARK_HANDLER = require('./bench.master.handler')

/**
 * Mean value of `n` times executed `function`
 * @param {Number} n times
 * @param  {...any} args 
 */
const processStruct =
  (n, fnc, ...args) =>
    R.compose(
      N_BENCHMARK_HANDLER.calculateMeanBench,
      N_BENCHMARK_HANDLER.processTimedResult,
      () => N_BENCHMARK_HANDLER.replicateExecution(
        n,
        N_BENCHMARK_HANDLER.timedFnc,
        fnc,
        ...args
      )
    )()

/**
 * @param {String} marker 
 * @param {String} comments `marker` comments 
 * @param {Function} fnc `function` for measuring
 * @param  {...any} args 
 * @returns `fnc(...args)` result
 */
const baseTimedFncIO =
  (marker, comments, fnc, ...args) =>
    M.IO(() => console.time(`${marker}${H.getTabSequence(marker)}${comments}`)
    ).takeRight(
      M.IO(() => fnc(...args))
    ).bind(
      (fncResult) =>
        M.IO(
          () => [
            fncResult,
            console.timeEnd(`${marker}${H.getTabSequence(marker)}${comments}`)
          ]
        )
    ).bind(
      ([fncResult, _]) => M.IO(() => fncResult)
    ).run()

module.exports = {
  processStruct,
  baseTimedFncIO
}
