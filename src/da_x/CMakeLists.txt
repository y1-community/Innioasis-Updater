cmake_minimum_required(VERSION 3.23)
#
# CMake Toolchain file for crosscompiling on ARM.
#
# Target operating system name.
set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_SYSTEM_PROCESSOR arm)

# Name of C compiler.
set(CMAKE_C_COMPILER "/usr/bin/arm-linux-gnueabihf-gcc-12")
set(CMAKE_C_OBJCOPY "/usr/bin/arm-linux-gnueabihf-objcopy")
set(CMAKE_C_SIZE "/usr/bin/arm-linux-gnueabihf-size")

set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_PACKAGE ONLY)

enable_language(C ASM)

project(mtk_payload)
set(CMAKE_C_FLAGS "-std=gnu99 -Os -mthumb -mcpu=cortex-a9 -fno-builtin-printf -fno-strict-aliasing -fno-builtin-memcpy -fno-stack-protector -fPIE -Wall -Wextra -z noexecstack")
set(CMAKE_ASM_FLAGS "${CMAKE_C_FLAGS}" )
set(CMAKE_EXE_LINKER_FLAGS "-nodefaultlibs -nostdlib -Wl,--build-id=none")
add_library(mycrt0 common/start.S)

add_executable(da_x.elf da_x.c)
target_sources(da_x.elf PRIVATE crypto/dxcc.c crypto/hmac-sha256.c crypto/sej.c crypto/sha256.c crypto/V5/rpmb.c common/flash_handler.c common/libc.c)
target_link_libraries(da_x.elf mycrt0)
set_target_properties(da_x.elf PROPERTIES LINK_DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/${LINKER_SCRIPT})
target_link_options(da_x.elf PRIVATE "-T${CMAKE_CURRENT_SOURCE_DIR}/common/generic.ld")
target_link_options(da_x.elf PRIVATE "-L ${CMAKE_BINARY_DIR}")
add_custom_target(da_x.bin ALL DEPENDS da_x.elf)
add_custom_command(TARGET da_x.elf POST_BUILD
        COMMAND ${CMAKE_C_OBJCOPY} -O binary $<TARGET_FILE:da_x.elf> ${CMAKE_CURRENT_SOURCE_DIR}/../../mtkclient/payloads/da_x.bin
        COMMAND ${CMAKE_C_SIZE} $<TARGET_FILE:da_x.elf>)
target_compile_options(da_x.elf PRIVATE -DV5)
