const I = require('immutable')
const H = require('../../../utils/general.helper')
const M = require('monet')
const FS = require('fs')
const MORI = require('mori')

/**
 * @param {Number} iterations 
 * @param {I.List|Array|ArrayLike} struct 
 * @param {Function} fnc Mapping `function`
 * @returns {I.List|Array|ArrayLike} processed `struct`
 */
const repeatMap =
  (iterations, struct, fnc) =>
    iterations > 0
      ? repeatMap(iterations - 1, struct.map(fnc), fnc)
      : struct

/**
 * Mori special repeat mapping 
 * @param {Number} iterations 
 * @param {ArrayLike} struct Mori `structure`
 * @param {Function} fnc Mapping `function`
 * @returns {ArrayLike} processed `struct`
 */
const repeatMoriMap =
  (iterations, struct, fnc) =>
    iterations > 0
      ? repeatMoriMap(iterations - 1, MORI.map(fnc, struct), fnc)
      : struct

/**
 * Write data in file with specific name if `true`
 * @param {Boolean} isFile 
 * @param {String} data Logs
 * @param {String} suite 
 * @param {String} specificity 
 */
const whenFlagWriteFile =
  (isFile, data, suite, specificity) =>
    isFile
      ? FS.existsSync(`${require.main.path}/../log/${specificity}`)
        ? FS.writeFileSync(`${require.main.path}/../log/${specificity}/${suite}.log`, data, { flag: 'as' })
        : M.IO(
          () => FS.mkdirSync(`${require.main.path}/../log/${specificity}`, { recursive: true })
        ).takeRight(
          M.IO(() => FS.writeFileSync(`${require.main.path}/../log/${specificity}/${suite}.log`, data, { flag: 'as' }))
        ).run()
      : H.trace(data)

module.exports = {
  whenFlagWriteFile,
  repeatMoriMap,
  repeatMap
}
