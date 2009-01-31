%define version	3.1.1
%define release	%mkrel 11

Name:		scim-fcitx
Summary:	SCIM IMEngine module for fcitx
Version:		%{version}
Release:		%{release}
Group:		System/Internationalization
License:		GPL
URL:			http://www.magiclinux.org/people/sunmoon1997/stuff/fcim/
Source0:		%{name}-%{version}.tar.bz2
Patch0:		scim-fcitx-3.1.1-gcc4.3.patch
Patch1:		scim-fcitx-3.1.1-libtool-flags.patch
Patch2:		scim-fcitx-3.1.1-linkage.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:			scim >= 1.4.0
BuildRequires:		scim-devel >= 1.4.7-4mdk
BuildRequires:		automake, libltdl-devel
Obsoletes:	%mklibname scim-fcitx 0

%description
Scim-fcitx is an SCIM IMEngine module for fcitx.
It supports Chinese input.

%prep
%setup -q -n fcitx
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
./bootstrap
%configure2_5x --disable-ltdl-install
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unnecessary files
rm -f %{buildroot}/%{scim_plugins_dir}/*/*.{a,la}

# we don't need to pack up the binary tools
rm -f %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_datadir}/scim/fcitx
%{_datadir}/scim/icons/fcitx
%{scim_plugins_dir}/IMEngine/*.so
