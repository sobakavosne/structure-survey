#include <napi.h>

Napi::Value Identity(const Napi::CallbackInfo &info)
{
  return Napi::Value(info.Env(), info[0]);
}