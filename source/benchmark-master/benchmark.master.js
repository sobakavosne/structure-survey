require('module-alias/register')

const H = require('@general-helper')
const R = require('ramda')
const N_BENCHMARK_HANDLER = require('./benchmark.master.handler')

/**
 * Mean value of `n` times executed `function`
 * @param {Number} n times
 * @param  {...any} args 
 */
const getMeanBenchmark =
  (n, fnc, ...args) =>
    R.compose(
      R.divide(R.__, n),
      R.sum,
      H.trace,
      () => N_BENCHMARK_HANDLER.replicateExecution(
        n,
        N_BENCHMARK_HANDLER.timedFnc,
        fnc,
        ...args
      )
    )()

module.exports = {
  getMeanBenchmark
}

// H.trace(Array(10).fill(0).map(x => timedFnc(() => nativeList.map(x => x))))
