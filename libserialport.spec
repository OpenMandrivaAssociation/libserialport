%define major 0
%define libname %mklibname serialport %{major}
%define devname %mklibname -d serialport

Name:           libserialport
Version:        0.1.1
Release:        10%{?dist}
Summary:        Library for accessing serial ports
License:        LGPLv3+
URL:            http://sigrok.org/wiki/%{name}
Source0:        http://sigrok.org/download/source/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  graphviz

Provides: bundled(jquery) = 1.7.1

%description
libserialport is a minimal library written in C that is intended to take care
of the OS-specific details when writing software that uses serial ports.

By writing your serial code to use libserialport, you enable it to work
transparently on any platform supported by the library.

The operations that are supported are:

- Port enumeration (obtaining a list of serial ports on the system).
- Opening and closing ports.
- Setting port parameters (baud rate, parity, etc).
- Reading, writing and flushing data.
- Obtaining error information.

%package  -n	%{libname}
Summary:        Development files for %{name}

%description -n	%{libname}
Library for accessing serial ports

%package  -n	%{devname}
Summary:        Development files for %{name}
Requires:       %{libname} = %{EVRD}

%description -n	%{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for developing software
with %{name}.


%prep
%setup -q

%build
%configure --disable-static
V=1 make %{?_smp_mflags}

# This builds documentation for the -doc package
make %{?_smp_mflags} doc


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files -n %{libname}
%{_libdir}/%{name}.so.0*

%files -n %{devname}
%doc COPYING README
%{_includedir}/%{name}.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so

%files doc
%doc doxy/html-api/
