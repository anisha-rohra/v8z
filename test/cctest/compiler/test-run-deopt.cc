#pragma convert("ISO8859-1")
// Copyright 2014 the V8 project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "src/v8.h"

#include "test/cctest/compiler/function-tester.h"

using namespace v8::internal;
using namespace v8::internal::compiler;

#if V8_TURBOFAN_TARGET

TEST(TurboSimpleDeopt) {
  FLAG_allow_natives_syntax = true;
  FLAG_turbo_deoptimization = true;

  FunctionTester T(
      "(function f(a) {"
      "var b = 1;"
      "if (!%IsOptimized()) return 0;"
      "%DeoptimizeFunction(f);"
      "if (%IsOptimized()) return 0;"
      "return a + b; })");

  T.CheckCall(T.Val(2), T.Val(1));
}


TEST(TurboSimpleDeoptInExpr) {
  FLAG_allow_natives_syntax = true;
  FLAG_turbo_deoptimization = true;

  FunctionTester T(
      "(function f(a) {"
      "var b = 1;"
      "var c = 2;"
      "if (!%IsOptimized()) return 0;"
      "var d = b + (%DeoptimizeFunction(f), c);"
      "if (%IsOptimized()) return 0;"
      "return d + a; })");

  T.CheckCall(T.Val(6), T.Val(3));
}

#endif

TEST(TurboTrivialDeopt) {
  FLAG_allow_natives_syntax = true;
  FLAG_turbo_deoptimization = true;

  FunctionTester T(
      "(function foo() {"
      "%DeoptimizeFunction(foo);"
      "return 1; })");

  T.CheckCall(T.Val(1));
}
