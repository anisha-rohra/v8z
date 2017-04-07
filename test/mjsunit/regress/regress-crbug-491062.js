// Copyright 2015 the V8 project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Flags: --allow-natives-syntax --stack-size=500

function g() {}

var count = 0;
function f() {
  try {
    f();
  } catch(e) {
    print(e.stack);
  }
  if (count < 500) {
    count++;
    %DebugGetLoadedScripts();
  }
}
f();
g();
