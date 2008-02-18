%define version	3.1.1
%define release	%mkrel 7

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:		scim-fcitx
Summary:	SCIM IMEngine module for fcitx
Version:		%{version}
Release:		%{release}
Group:		System/Internationalization
License:		GPL
URL:			http://www.magiclinux.org/people/sunmoon1997/stuff/fcim/
Source0:		%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:			%{libname} = %{version}-%{release}
Requires:			scim >= %{scim_version}
BuildRequires:		scim-devel >= 1.4.7-4mdk
BuildRequires:		automake, libltdl-devel

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
%setup -q -n fcitx

%build
./bootstrap
%configure2_5x
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

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_datadir}/scim/fcitx
%{_datadir}/scim/icons/fcitx

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{scim_plugins_dir}/IMEngine/*.so
