
py_binary(
    name = 'complex_bin',
    main = 'complex_bin.py',
    srcs = ['complex_bin.py'],
    deps = [":complex_lib"]
)

py_library(
    name = 'complex_lib',
    srcs = ['complex_lib.py'],
)

py_test(
    name = "complex_test",
    srcs = ["complex_test.py"],
    deps = ["complex_lib"],
)
