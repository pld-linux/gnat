Summary:	GNAT Ada 95 Compiler
Summary(pl):	GNAT - kompilator jêzyka Ada 95
Name:		gnat
Version:	3.15p
Release:	0.2
Epoch:		0
License:	GPL v2
Group:		Development/Languages
Vendor:		Ada Core Technologies
Source0:	http://libre.act-europe.fr/GNAT/%{version}/%{name}-%{version}-i686-pc-redhat71-gnu-bin.tar.gz
# Source0-md5:	57c060cd1ccef8b1ae9165b11d98780a
#SourceX:	sparc, alpha, ppc?
#Source10:	http://libre.act-europe.fr/GNAT/%{version}/%{name}-%{version}-unx-docs.tar.gz
#Source11:	http://libre.act-europe.fr/GNAT/%{version}/%{name}-%{version}-src.tgz
URL:		http://libre.act-europe.fr/GNAT/main.html
Requires(post,postun):	/sbin/ldconfig
ExclusiveArch:	i686
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/opt/gnat
%define		_gcclib		%{_prefix}/lib/gcc-lib

%description
GNAT is a complete Ada 95 compilation system, maintained and
distributed under the GNU General Public License by Ada Core
Technologies.

%description -l pl
GNAT to kompletny system kompilatora dla jêzyka Ada 95, utrzymywany i
rozpowszechniany na licencji GNU GPL przez Ada Core Technologies.

%prep
%ifarch i686
%define _base_name i686-pc-linux-gnu-bin
%{__tar} -xzf %{SOURCE0}
%endif
%setup -qDTn %{name}-%{version}-%{_base_name}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} ins-all \
	prefix=$RPM_BUILD_ROOT%{_prefix}

rm -rf $RPM_BUILD_ROOT%{_prefix}/doc
rm -rf $RPM_BUILD_ROOT%{_prefix}/bin/{{,real/}gvd,gnathtml.pl}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%dir %{_bindir}
%dir %{_bindir}/real
%attr(755,root,root) %{_bindir}/.gnat_wrapper
%attr(755,root,root) %{_bindir}/addr2line
%attr(755,root,root) %{_bindir}/g*
%attr(755,root,root) %{_bindir}/real/*
%dir %{_prefix}/lib/gcc-lib/*/2.8.1
%{_prefix}/lib/gcc-lib/*/2.8.1/adainclude
%{_prefix}/lib/gcc-lib/*/2.8.1/adalib
%{_prefix}/lib/gcc-lib/*/2.8.1/include
%{_prefix}/lib/gcc-lib/*/2.8.1/rts-fsu
%{_prefix}/lib/gcc-lib/*/2.8.1/rts-native
%{_prefix}/lib/gcc-lib/*/2.8.1/*.[ao]
%attr(755,root,root) %{_prefix}/lib/gcc-lib/*/2.8.1/cc1
%attr(755,root,root) %{_prefix}/lib/gcc-lib/*/2.8.1/cpp
%attr(755,root,root) %{_prefix}/lib/gcc-lib/*/2.8.1/gnat1
%{_prefix}/lib/gcc-lib/*/2.8.1/specs
