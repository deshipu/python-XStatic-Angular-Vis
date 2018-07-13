%if 0%{?fedora}
%global with_python3 1
%endif

%global pypi_name XStatic-Angular-Vis

Name:           python-%{pypi_name}
Version:        4.16.0.0
Release:        1%{?dist}
Provides:       python2-XStatic-Angular-Vis = %{version}-%{release}
Summary:        Angular-Vis (XStatic packaging standard)

License:        MIT
URL:            https://github.com/visjs/angular-visjs
Source0:        https://files.pythonhosted.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

Requires:       python-XStatic
Requires:       xstatic-angular-vis-common


%description
Angular-Vis JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.


%package -n xstatic-angular-vis-common
Summary:        %{summary}

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-angular-vis-common
Angular-Vis JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package contains the JavaScript files.


%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-XStatic
Requires:       xstatic-angular-vis-common

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Angular-Vis JavaScript library packaged for setup-tools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package provides Python 3 build of %{pypi_name}.
%endif


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/angular_vis'|" xstatic/pkg/angular_vis/__init__.py


%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif


%install
%py2_install
mkdir -p %{buildroot}/%{_jsdir}/angular_vis
mv %{buildroot}/%{python2_sitelib}/xstatic/pkg/angular_vis/data/angular-vis.js %{buildroot}/%{_jsdir}/angular_vis
rmdir %{buildroot}%{python2_sitelib}/xstatic/pkg/angular_vis/data/

%if 0%{?with_python3}
%py3_install
# Remove static files, already created by the python2 subpkg
rm -rf %{buildroot}%{python3_sitelib}/xstatic/pkg/angular_uuid/data/
%endif


%files -n python-%{pypi_name}
%doc README.txt
%{python2_sitelib}/xstatic/pkg/angular_vis
%{python2_sitelib}/XStatic_Angular_Vis-%{version}-py%{python_version}.egg-info
%{python2_sitelib}/XStatic_Angular_Vis-%{version}-py%{python_version}-nspkg.pth

%files -n xstatic-angular-vis-common
%doc README.txt
%{_jsdir}/angular_vis

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/xstatic/pkg/angular_vis
%{python3_sitelib}/XStatic_Angular_Vis-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/XStatic_Angular_Vis-%{version}-py%{python3_version}-nspkg.pth
%endif

%changelog
* Thu Jul 12 2018 Radomir Dopieralski <rdopiera@redhat.com) - 4.16.0.0-1
- Initial package
