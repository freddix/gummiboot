Summary:	Simple text-mode UEFI Boot Manager
Name:		gummiboot
Version:	33
Release:	1
License:	LGPL
Group:		Applications/System
Source0:	http://cgit.freedesktop.org/gummiboot/snapshot/%{name}-%{version}.tar.gz
# Source0-md5:	3178264ee552ec74852559e4301b01fe
URL:		http://freedesktop.org/wiki/Software/gummiboot
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnu-efi
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple UEFI boot manager.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/gummiboot update >/dev/null 2>&1 || :

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/gummiboot
%dir %{_prefix}/lib/gummiboot
%ifarch %{x8664}
%{_prefix}/lib/gummiboot/gummibootx64.efi
%else
%{_prefix}/lib/gummiboot/gummibootia32.efi
%endif
%{_mandir}/man8/gummiboot.8*

