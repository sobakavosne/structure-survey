#include <napi.h>
#include <math.h>

Napi::Value Add(const Napi::CallbackInfo &info)
{
  Napi::Env env = info.Env();
  int a = int(info[0].ToNumber());
  int b = int(info[1].ToNumber());

  return Napi::Value(info.Env(), Napi::Number::New(env, a + b));
}