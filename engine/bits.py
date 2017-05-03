# -*- coding: utf-8 -*-
#
# ibus-replace-with-kanji - Replace With Kanji input method for IBus
#
# Using source code derived from
#   ibus-tmpl - The Input Bus template project
#
# Copyright (c) 2017 Esrille Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# EngineReplaceWithKanji.__modifiers bits
ShiftL_Bit = 1 << 0
ShiftR_Bit = 1 << 1
ControlL_Bit = 1 << 2
ControlR_Bit = 1 << 3
Space_Bit = 1 << 4
Henkan_Bit = 1 << 5
Muhenkan_Bit = 1 << 6

Dual_Space_Bit = 1 << 8
Dual_ShiftR_Bit = 1 << 9
Dual_ControlR_Bit = 1 << 10
Dual_Henkan_Bit = 1 << 11
Dual_Muhenkan_Bit = 1 << 12

Not_Dual_Space_Bit = 1 << 16
Not_Dual_ShiftR_Bit = 1 << 17
Not_Dual_ControlR_Bit = 1 << 18
Not_Dual_Henkan_Bit = 1 << 19
Not_Dual_Muhenkan_Bit = 1 << 20