REM ========================================================
REM Install libzim
git clone https://github.com/openzim/libzim.git || exit /b 1
cd libzim
git checkout 8.0.0 || exit /b 1
meson . build --prefix %EXTRA_DIR% --default-library static --buildtype release || exit /b 1
cd build
ninja || exit /b 1
ninja install || exit /b 1
cd ..\..
