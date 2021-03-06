{
    'targets':
    [
        {
            'target_name': 'addon',
            'include_dirs': ['./v8pp'],
            'cflags_cc': ['-std=c++11', '-fexceptions'],
            'msvs_settings': { 'VCCLCompilerTool': { 'ExceptionHandling': 1 } },
            'xcode_settings': { 'GCC_ENABLE_CPP_EXCEPTIONS': 'YES' },
            'sources': ['src/addon.cc'],
        }
    ]
}
