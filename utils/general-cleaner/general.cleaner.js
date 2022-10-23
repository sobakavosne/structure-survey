const FS = require('fs')

/**
 * @param {Array<String>} tmpDirs
 */
const clearTmpDirIO =
  (...tmpDirs) =>
    tmpDirs.map(
      tmpDir => FS.rmdirSync(tmpDir, { recursive: true, force: true }),
      () => tmpDirs
    )

module.exports = {
  clearTmpDirIO
}
