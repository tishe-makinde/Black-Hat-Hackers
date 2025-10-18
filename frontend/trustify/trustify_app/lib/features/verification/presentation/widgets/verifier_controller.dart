import 'package:flutter/cupertino.dart';
import 'package:trustify_app/features/verification/presentation/enums/verifier_type.dart';
import 'package:trustify_app/features/verification/presentation/pages/image_verifier_page.dart';
import 'package:trustify_app/features/verification/presentation/pages/link_verifier_page.dart';

class VerifierController extends StatelessWidget {
  final VerifierType selectedVerifier;
  const VerifierController({
    super.key,
    required this.selectedVerifier,
  });

  @override
  Widget build(BuildContext context) {
    switch (selectedVerifier) {
      case VerifierType.link:
        return LinkVerifierPage();
      case VerifierType.image:
        return ImageVerifierPage();
    }
  }
}
