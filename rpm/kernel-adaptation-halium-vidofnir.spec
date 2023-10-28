# Device details
%define device halium-vidofnir

# Kernel target architecture
%define kernel_arch arm64

%define kcflags "KCFLAGS=-Wno-incompatible-library-redeclaration -Wno-bitwise-instead-of-logical -Wno-fortify-source -Wno-unused-but-set-variable -Wno-error=unused-but-set-variable"

#Compiler to use
%define compiler CC=clang
%define compileropts CLANG_TRIPLE=aarch64-linux-gnu- LLVM=1 LLVM_IAS=1 V=1 HOSTLDFLAGS="-fuse-ld=lld" CROSS_COMPILE=aarch64-linux-android- CROSS_COMPILE_ARM32=arm-linux-androideabi-
#define compiler #{nil}
#define compileropts #{nil}

# Crossbuild toolchain to use
#define crossbuild aarch64

# RPM target architecture, remove to leave it unaffected
# You should have a good reason to change the target architecture
# (like building on aarch64 targeting an armv7hl repository)
%define device_target_cpu aarch64

# Defconfig to pick-up
%define defconfig sfos-gx4_defconfig

# Linux kernel source directory
%define source_directory linux/

# Build modules
%define build_modules 1

# Build Image
%define build_Image 1

# Apply Patches
%define apply_patches 1

%define ramdisk ramdisk-vidofnir.img
##define build_dtboimg 1

# Build and pick-up the following devicetrees
##define devicetrees

#Device Info
%define deviceinfo_kernel_cmdline bootopt=64S3,32N2,64N2 systempart=/dev/mapper/system
%define deviceinfo_dtb mediatek/mt6789.dtb
%define deviceinfo_flash_pagesize 4096
%define deviceinfo_flash_offset_base 0x0
%define deviceinfo_flash_offset_kernel 0x40000000
%define deviceinfo_flash_offset_ramdisk 0x66f00000
%define deviceinfo_flash_offset_tags 0x47c80000
%define deviceinfo_flash_offset_dtb 0x47c80000
%define deviceinfo_bootimg_qcdt false
%define deviceinfo_bootimg_header_version 4
%define deviceinfo_bootimg_partition_size 67108864
%define deviceinfo_bootimg_os_version 12
%define deviceinfo_bootimg_os_patch_level 2022-06
%define deviceinfo_rootfs_image_sector_size 4096
%define deviceinfo_halium_version 12

%include kernel-adaptation-simplified/kernel-adaptation-simplified.inc
