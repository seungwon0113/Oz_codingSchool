# Django
**Python Django**

- **특징 및 대표적인 모듈:**
    - Django는 Python 기반의 웹 프레임워크로, 고수준의 웹 개발을 위한 기능을 포괄적으로 제공합니다.
    - 대표적인 모듈로는 ORM(객체 관계 매핑), MTV(Model-Template-View) 아키텍처, Django REST framework(RESTful API 개발) 등이 있습니다.
- **장점:**
    - 기본적인 기능들이 이미 내장되어 있어 빠르게 개발을 시작할 수 있습니다.
    - 강력한 ORM 기능으로 데이터베이스 작업이 편리합니다.


## pyproject.toml
<img src="screenshot/스크린샷 2024-09-10 오후 4.53.34.png">
   
    [tool.poetry] 
    name = "django"
    version = "0.1.0"
    description = "python django project"
    authors = ["관리자 이름 <관리자 이메일>"]
    readme = "README.md"

    [tool.poetry.dependencies]
    python = "^3.12"

    [build-system]
    requires = ["poetry-core"]
    build-backend = "poetry.core.masonry.api"
    
\
**`poetry init`** 명령을 실행하면, **`pyproject.toml`** 파일을 설정하는 과정이 시작됩니다.

**`pyproject.toml`** 파일은 프로젝트의 메타데이터와 의존성을 관리하는 데 사용되며, Poetry를 사용하는 Python 프로젝트의 핵심 구성 파일입니다.

1. **Package Name**: 프로젝트 또는 패키지의 이름입니다. 일반적으로 프로젝트의 디렉토리 이름을 기본값으로 사용합니다.
2. **Version**: 패키지의 시작 버전입니다. 일반적으로 **`0.1.0`**으로 시작하며, 개발 진행에 따라 버전을 업데이트합니다.
3. **Description**: 프로젝트의 간단한 설명입니다. 이 내용은 PyPI 등의 패키지 저장소에 표시됩니다.
4. **Author Name**: 패키지의 작성자 또는 유지 관리자의 이름입니다. 이 정보는 선택 사항이지만, 공개 패키지의 경우 중요할 수 있습니다.
5. **License**: 프로젝트에 적용할 라이선스입니다. Open Source 프로젝트의 경우, 일반적으로 MIT, GPL, Apache 등의 라이선스를 사용합니다.
6. **Python Version Compatibility**: 프로젝트가 호환되는 Python 버전을 지정합니다. 예를 들어, **`^3.7`**은 Python 3.7 이상의 버전과 호환됨을 의미합니다.
7. **Dependency Specification**: 프로젝트의 의존성을 지정합니다. 필요한 외부 패키지를 여기에 추가할 수 있습니다.
8. **Development Dependency Specification**: 개발 시에만 필요한 의존성을 지정합니다. 예를 들어, 테스팅 라이브러리나 문서화 도구 등이 여기에 해당됩니다.

설정이 완료되면, **`pyproject.toml`** 파일이 프로젝트의 루트 디렉토리에 생성됩니다. 이 파일은 프로젝트의 구성을 정의하고, Poetry가 패키지 관리를 수행하는 데 필요한 모든 정보를 포함합니다.

추가적으로, Poetry는 **`poetry.lock`** 파일을 생성하여 프로젝트의 의존성 트리를 정확하게 재현할 수 있게 해줍니다. 이는 프로젝트가 다양한 환경에서도 동일한 방식으로 작동하도록 보장합니다.

## poetry.lock
<img src="screenshot/스크린샷 2024-09-11 오전 10.22.02.png">

    [[package]]
    name = "asgiref"
    version = "3.8.1"
    description = "ASGI specs, helper code, and adapters"
    optional = false
    python-versions = ">=3.8"
    files = [
        {file = "asgiref-3.8.1-py3-none-any.whl", hash = "sha256:3e1e3ecc849832fe52ccf2cb6686b7a55f82bb1d6aee72a58826471390335e47"},
        {file = "asgiref-3.8.1.tar.gz", hash = "sha256:c343bd80a0bec947a9860adb4c432ffa7db769836c64238fc34bdc3fec84d590"},
    ]
- 위의 내용처럼 **`Django`** 에서 지원하는 **`package`** 가 포함되어 있는 파일
- **`poetry.lock`** 파일은 프로젝트의 의존성 트리에 대한 정확한 스냅샷을 제공합니다. 이 파일은 **`poetry add`** 명령을 사용하여 의존성을 추가할 때마다 생성되거나 업데이트됩니다.
- 이 파일은 프로젝트가 사용하는 모든 패키지의 정확한 버전을 기록하며, 프로젝트를 다른 환경에서 재생성할 때 동일한 의존성을 보장합니다.
- **`poetry.lock`** 파일을 소스 코드 저장소에 포함시켜 다른 개발자나 배포 환경에서도 동일한 의존성을 사용하도록 할 수 있습니다.
- 이 파일은 직접 편집하는 것이 아니라, Poetry 명령어를 통해 간접적으로 관리됩니다.
