<!--next-version-placeholder-->

## v0.3.0 (2022-09-21)
### Feature
* Rename package to avoid clash on pypi ([`3efe5bf`](https://github.com/mblackgeo/fast-geodist/commit/3efe5bff57296d5e14c3491583ae863ddba68aac))

### Documentation
* Remove completed items from roadmap ([`d4aad2e`](https://github.com/mblackgeo/fast-geodist/commit/d4aad2e14aa0cd717f006d2b5771b1330fc9a477))
* Add badges ([`6dd65c4`](https://github.com/mblackgeo/fast-geodist/commit/6dd65c48d644849752973d182c6af2a17c7ee3f9))
* Rename package ([`dc00675`](https://github.com/mblackgeo/fast-geodist/commit/dc006755489e7a4fd7d3843a081c05d57e35dfc1))
* Add todo for package rename ([`5f5f490`](https://github.com/mblackgeo/fast-geodist/commit/5f5f490ed58383f3265eab933e58569899b49b85))
* Fix spacing in example ([`03d6a8c`](https://github.com/mblackgeo/fast-geodist/commit/03d6a8c0221c8f3e962359a4feb1468ea4ece2dd))
* Add install command ([`dd45b54`](https://github.com/mblackgeo/fast-geodist/commit/dd45b54f055342157f41ea4d71b3a994cfad9184))

## v0.2.0 (2022-09-15)
### Feature
* Rename internal rust package ([`16e61db`](https://github.com/mblackgeo/fast-geodist/commit/16e61db3c3609127470458ef82749d6a6b19344e))

## v0.1.0 (2022-09-15)
### Feature
* First release ([`7a2067d`](https://github.com/mblackgeo/fast-geodist/commit/7a2067dd9688017609463f93df26d2acc388d69a))
* Add CD pipeline and semantic release ([#2](https://github.com/mblackgeo/fast-geodist/issues/2)) ([`f492491`](https://github.com/mblackgeo/fast-geodist/commit/f492491062fe919a6a6b67ae46621917d379993e))
* Add a conveient python wrapper around the rust functions ([`9e12458`](https://github.com/mblackgeo/fast-geodist/commit/9e12458ca4cf495db090e6a571c6142d3b0ef2f6))
* Implement numpy wrapper for array distance calculation ([`0932b84`](https://github.com/mblackgeo/fast-geodist/commit/0932b848ef03a6a0bf9fbe80d1eb58b3a64b5b09))
* Add an array implementation of haversine distance ([`c78bfb1`](https://github.com/mblackgeo/fast-geodist/commit/c78bfb11e805e0b4408610c9fb578989827431ba))
* Increase the amount data used for benchmarking ([`a3fb8a5`](https://github.com/mblackgeo/fast-geodist/commit/a3fb8a552cb654cff8d7142f0403c8b0b11e6fe9))
* Add implementation that works with a vector of coords ([`446ed5f`](https://github.com/mblackgeo/fast-geodist/commit/446ed5f0f605fb6f4603f89d9261d10dc8d494a2))
* Add python haversine function ([`dd74843`](https://github.com/mblackgeo/fast-geodist/commit/dd74843c80e38452d193dc2574d7874ad56006bb))
* Implement algo following georust ([`056b047`](https://github.com/mblackgeo/fast-geodist/commit/056b047c61ab97b4fd59a6aa2cc06e7469a9d933))
* Add wireframe of rust package ([`e6b8e67`](https://github.com/mblackgeo/fast-geodist/commit/e6b8e67d99b6f1c8edcfa817ead4bedb31f4ef0b))

### Fix
* Allocate an empty vector without size ([`c1b0437`](https://github.com/mblackgeo/fast-geodist/commit/c1b04371f3b973af0a6014aca5830f3bd59e7d16))
* Use python 3.7 compatible type hints ([`29f0772`](https://github.com/mblackgeo/fast-geodist/commit/29f07721faec6d3581a4c448273c5151682af638))

### Documentation
* Add benchmark results ([`f37c2d9`](https://github.com/mblackgeo/fast-geodist/commit/f37c2d99cd65921ce3b26e0aacdd3236ce58e819))
* Correct minor typos ([`a6b054f`](https://github.com/mblackgeo/fast-geodist/commit/a6b054fba9fed2181ce620f7de47dcdeda125c04))
* Fix broken link ([`b824b45`](https://github.com/mblackgeo/fast-geodist/commit/b824b45291742de0d183849189af4b898f76c4f4))
* Update notes for use with np.array ([`96201d4`](https://github.com/mblackgeo/fast-geodist/commit/96201d4a264edce9f8633c7d2e19d59a5b908503))
* Remove pre-commit as a prerequisite ([`6828eec`](https://github.com/mblackgeo/fast-geodist/commit/6828eec1acd816e65d0168b0b0ccf5a352358ee6))
* Populate README with full instructions ([`7a240fc`](https://github.com/mblackgeo/fast-geodist/commit/7a240fc5a7851d9ffbf90a37008b37141ed287b3))
* Mark tasks complete ([`dd911e0`](https://github.com/mblackgeo/fast-geodist/commit/dd911e0a3fd7a7a47f3ba549e8345dd0bf6e1432))
* Typo ([`a93ad51`](https://github.com/mblackgeo/fast-geodist/commit/a93ad517db6df30b7a3d993b0f29ba72d181076d))
* Add helpful links ([`141cea4`](https://github.com/mblackgeo/fast-geodist/commit/141cea431cd295703fc73bf91d10155d8e64724e))
* Add more TODOs ([`3725bcc`](https://github.com/mblackgeo/fast-geodist/commit/3725bcc218eb6414756f07bdb55afd031ec4090c))
* Add note to add more docs ([`eeda04a`](https://github.com/mblackgeo/fast-geodist/commit/eeda04a0ae6d33b56408414966d4692d9bba9b47))
* Add TODO list ([`df0e33b`](https://github.com/mblackgeo/fast-geodist/commit/df0e33bd5093ed101aca775cce095e4907d093eb))

### Performance
* Update benchmark ([`86e73d8`](https://github.com/mblackgeo/fast-geodist/commit/86e73d813285bee1d71a28e759658006cba75bc5))
* Update benchmark to work with numpy arrays ([`1ea2c02`](https://github.com/mblackgeo/fast-geodist/commit/1ea2c02cec1da538f76487ec2fef98d07cd1e6d9))
* Preallocate the vector with type and size ([`ab8b2b2`](https://github.com/mblackgeo/fast-geodist/commit/ab8b2b24e9c3fe809fd367b92dda86a94d71b60d))
* Add benchmarks ([`b42a87a`](https://github.com/mblackgeo/fast-geodist/commit/b42a87adfcbeb2e1c039528a602f43d609c7c06c))
* Add pytest-benchmark ([`223c602`](https://github.com/mblackgeo/fast-geodist/commit/223c6026aa4925e8f2c34e1082a8ea7ca814a5b5))