%define octpkg interval

# Exclude .oct files from provides
%define __provides_exclude_from ^%{octpkglibdir}/.*.oct$

Summary:	Evaluate functions over subsets of their domain with Octave
Name:		octave-%{octpkg}
Version:	2.1.0
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPL-3.0+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 3.8.0
BuildRequires:	mpfr-devel

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

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}-%{version}/NEWS
%doc %{octpkg}-%{version}/COPYING

