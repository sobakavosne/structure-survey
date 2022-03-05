const R = require('ramda')
const M = require('monet')

/**
 * Tracing function for embedding
 * @param {Object} x Traced parameter
 * @param  {...any} comments Untraced comments
 * @returns `x`
 */
const trace =
  (x, ...comments) =>
    M.IO(
      () => console.log(x, ...comments)
    ).takeRight(
      M.IO(() => x)
    ).run()

/**
 * @param {*} object 
 */
const eitherObjValuesToNumber =
  (object) =>
    R.mapObjIndexed(
      (value, key, obj) => Number(value) ? Number(value) : value,
      object
    )

/**
 * @param {Array} list 
 */
const eitherListValuesToNumber =
  (list) =>
    list.map(x => Number(x) ? Number(x) : x)

/**
 * @param {Number} number 
 */
const prettyInt =
  (number) =>
    R.compose(
      R.join(' '),
      R.map(R.join('')),
      R.map(R.reverse),
      R.reverse,
      R.splitEvery(3),
      R.reverse,
      R.split(''),
      R.toString
    )(number)

module.exports = {
  eitherListValuesToNumber,
  eitherObjValuesToNumber,
  prettyInt,
  trace
}