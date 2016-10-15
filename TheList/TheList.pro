CONFIG   += console
CONFIG   -= app_bundle

TEMPLATE = app
SOURCES += main.cpp \
    movie.cpp \
    customer.cpp \
    customerlist.cpp \
    movielist.cpp \
    pulllist.cpp


CONFIG += c++11

QMAKE_CXXFLAGS += -Wmissing-include-dirs
QMAKE_CXXFLAGS += -Wfloat-equal
QMAKE_CXXFLAGS += -Wredundant-decls
QMAKE_CXXFLAGS += -Winit-self
QMAKE_CXXFLAGS += -Wshadow
QMAKE_CXXFLAGS += -Wconversion

# QMAKE_CXXFLAGS += -Werror
# QMAKE_CXXFLAGS += -Wno-error=unused-variable

QMAKE_CXXFLAGS += -pedantic
QMAKE_CXXFLAGS += -pedantic-errors

HEADERS += \
    movie.h \
    customer.h \
    customerlist.h \
    movielist.h \
    pulllist.h

DISTFILES += \
    list.txt \
    topull.txt


