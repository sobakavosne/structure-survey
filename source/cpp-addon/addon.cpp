#include <napi.h>
#include "./lib/identity.cpp"
#include "./lib/add.cpp"

Napi::Object Initialize(Napi::Env env, Napi::Object exports)
{
  exports.Set("identity", Napi::Function::New(env, Identity));
  exports.Set("add", Napi::Function::New(env, Add));
  return exports;
}

NODE_API_MODULE(addon, Initialize)