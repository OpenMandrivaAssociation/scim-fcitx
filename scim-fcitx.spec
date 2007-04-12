%define version	3.1.1
%define release	%mkrel 6

%define scim_version	1.4.0

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:		scim-fcitx
Summary:	Scim-fcitx is an SCIM IMEngine module for fcitx
Version:		%{version}
Release:		%{release}
Group:		System/Internationalization
License:		GPL
URL:			http://www.magiclinux.org/people/sunmoon1997/stuff/fcim/
Source0:		%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:			%{libname} = %{version}
Requires:			scim >= %{scim_version}
BuildRequires:		scim-devel >= %{scim_version}
BuildRequires:		automake1.8, libltdl-devel

%description
Scim-fcitx is an SCIM IMEngine module for fcitx.
It supports Chinese input.


%package -n %{libname}
Summary:	Scim-fcitx library
Group:		System/Internationalization
Provides:		%{libname_orig} = %{version}-%{release}

%description -n %{libname}
scim-fcitx library.


%prep
%setup -q
cp /usr/share/automake-1.9/mkinstalldirs .

%build
[[ ! -x configure ]] && ./bootstrap
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unnecessary files
rm -f %{buildroot}/%{_libdir}/scim-1.0/*/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_datadir}/scim/fcitx/*
%{_datadir}/scim/icons/*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/scim-1.0/IMEngine/*.so


