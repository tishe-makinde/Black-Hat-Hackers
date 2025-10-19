import 'package:dartz/dartz.dart';
import 'package:trustify_app/core/error/failure.dart';
import 'package:trustify_app/core/usecase/usecase.dart';
import 'package:trustify_app/features/verification/domain/repository/verification_repository.dart';

class VerifyLinkUseCase implements UseCase<Map<String, dynamic>, String> {
  final VerificationRepository _verificationRepository;
  VerifyLinkUseCase(this._verificationRepository);
  @override
  Future<Either<Failure, Map<String, dynamic>>> call(String url) async {
    return await _verificationRepository.verifyLink(url);
  }
}
