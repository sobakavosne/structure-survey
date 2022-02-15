require('module-alias/register')

const H = require('@general-helper')
const ENV = H.eitherObjValuesToNumber(require('dotenv').config().parsed)
const DS_GEN = require('./data.struct.generator')

module.exports = {
  I_LIST: DS_GEN.constructImmutableList(ENV.STRUCT_SIZE),
  M_LIST: DS_GEN.constructMoriList(ENV.STRUCT_SIZE),
  N_LIST: DS_GEN.constructNativeList(ENV.STRUCT_SIZE),
  L_LIST: DS_GEN.constructLazyList(ENV.STRUCT_SIZE)
}