%global octpkg interval

Summary:	Evaluate functions over subsets of their domain with Octave
Name:		octave-%{octpkg}
Version:	3.2.1
Release:	1
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPL-3.0+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 4.2.0
BuildRequires:	pkgconfig(mpfr)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
The interval package for real-valued interval arithmetic allows
one to evaluate functions over subsets of their domain. All results are
verified, because interval computations automatically keep track of any
errors.
 
These concepts can be used to handle uncertainties, estimate arithmetic errors
and produce reliable results.  Also it can be applied to computer-assisted
proofs, constraint programming, and verified computing.
 
The implementation is based on interval boundaries represented by binary64
numbers and is conforming to IEEE Std 1788-2015, IEEE standard for interval
arithmetic.

This package is part of community Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
%set_build_flags
%ifarch %{x86_64}
export CC=gcc
export CXX=g++
%endif
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

