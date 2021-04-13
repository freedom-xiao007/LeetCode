package easy;/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import java.util.ArrayList;
import java.util.List;

/**
 * @author lw1243925457
 */
public class Solution509 {
    private List<Integer> cache = new ArrayList();

    public int fib(int n) {
        if (n < 2) {
            return n;
        }

        cache.add(0);
        cache.add(1);

        for (int i = 2; i < n; i++) {
            cache.add(cache.get(i-1) + cache.get(i-2));
        }
        return cache.get(n);
    }

    public static void main(String[] args) {
        Solution509 solution = new Solution509();
        assert solution.fib(2) == 1;
    }
}
