const H = require('../../../utils/general.helper')
const M = require('monet')
const FS = require('fs')
const MORI = require('mori')
const SG_STR_BUILDER = require('./suite.generator.str_builder')

/**
 * @param {Number} iterations 
 * @param {I.List|Array|ArrayLike} struct 
 * @param {Function} fnc Mapping `function`
 * @returns {I.List|Array|ArrayLike} processed `struct`
 */
const repeatMap =
  (iterations, struct, fnc) => iterations > 0
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
  (iterations, struct, fnc) => iterations > 0
    ? repeatMoriMap(iterations - 1, MORI.map(fnc, struct), fnc)
    : struct

/**
 * Write data in file with specific name if `true`
 * @param {Boolean} isFile 
 * @param {String} data Logs
 * @param {String} fncName 
 * @param {String} lib
 * @param {Number} iterations 
 * @param {Number} structSize 
 * @param {String} specificity 
 */
const whenFlagWriteFile =
  (isFile, data, fncName, lib, iterations, structSize, specificity) => isFile
    ? FS.existsSync(SG_STR_BUILDER.logDirBuilder(require.main.path, specificity))
      ? FS.writeFileSync(
        SG_STR_BUILDER.logFileNameBuilder(require.main.path, fncName, lib, iterations, structSize, specificity),
        data,
        { flag: 'as' }
      ) : M.IO(
        () => FS.mkdirSync(SG_STR_BUILDER.logDirBuilder(require.main.path, specificity), { recursive: true })
      ).takeRight(
        M.IO(
          () => FS.writeFileSync(
            SG_STR_BUILDER.logFileNameBuilder(require.main.path, fncName, lib, iterations, structSize, specificity),
            data,
            { flag: 'as' }
          )
        )
      ).run()
    : H.trace(data)

module.exports = {
  whenFlagWriteFile,
  repeatMoriMap,
  repeatMap
}